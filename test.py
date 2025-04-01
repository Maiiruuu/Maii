import sqlite3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import deque

# Initialiser la base de données SQLite
def init_database():
    conn = sqlite3.connect("site.sql")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            count INTEGER DEFAULT 0,
            visited BOOLEAN DEFAULT 0
        )
    """)
    conn.commit()
    return conn

# Ajouter ou mettre à jour un lien dans la base de données
def update_link(conn, url, visited=False):
    cursor = conn.cursor()
    cursor.execute("SELECT count FROM links WHERE url = ?", (url,))
    result = cursor.fetchone()

    if result:
        # Mettre à jour le nombre de fois croisé
        cursor.execute("""
            UPDATE links SET count = count + 1, visited = ? WHERE url = ?
        """, (visited, url))
    else:
        # Ajouter un nouveau lien
        cursor.execute("""
            INSERT INTO links (url, count, visited) VALUES (?, 1, ?)
        """, (url, visited))
    conn.commit()

# Récupérer les liens non visités
def get_unvisited_links(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM links WHERE visited = 0")
    return [row[0] for row in cursor.fetchall()]

# Fonction principale pour le crawling
def crawl_website(start_url, max_depth=2):
    conn = init_database()
    queue = deque([(start_url, 0)])
    visited = set()

    while queue:
        url, depth = queue.popleft()

        if depth > max_depth or url in visited:
            continue
        print(f"Exploring: {url}")
        visited.add(url)
        update_link(conn, url, visited=True)

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            next_url = urljoin(url, link['href'])

            # Ajouter ou mettre à jour le lien dans la base de données
            update_link(conn, next_url, visited=False)

            # Ajouter dans la file d'attente si non visité
            if next_url not in visited:
                queue.append((next_url, depth + 1))

    # Afficher les liens non visités
    unvisited_links = get_unvisited_links(conn)
    print(f"\nUnvisited links ({len(unvisited_links)}):")
    for link in unvisited_links:
        print(link)

    conn.close()

if __name__ == "__main__":
    start_url = input("Enter the starting URL: ")
    max_depth = int(input("Enter the crawling depth: "))
    crawl_website(start_url, max_depth)
