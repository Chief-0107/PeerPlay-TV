import os

DOMAIN = "https://peerplay-tv-app.github.io"
ACTORS_DIR = "actors"
JS_MAP_PATH = os.path.join("js", "actors-map.js")

if os.path.exists(ACTORS_DIR):
    actor_files = [f for f in os.listdir(ACTORS_DIR) if f.endswith('.html') and f != 'profile.html']
    
    actors_map = {}
    for filename in actor_files:
        parts = filename.replace('.html', '').split('-')
        if parts[-1].isdigit():
            actor_id = parts[-1]
            # 💡 Зберігаємо ТІЛЬКИ назву файлу без префікса actors/
            actors_map[actor_id] = filename

    os.makedirs("js", exist_ok=True)
    with open(JS_MAP_PATH, "w", encoding="utf-8") as f:
        f.write("// Карта акторів (чисті імена файлів без префікса actors/)\n")
        f.write("const generatedActorsMap = {\n")
        for aid, file_name in actors_map.items():
            f.write(f'  "{aid}": "{file_name}",\n')
        f.write("};\n")
        
    print(f"✅ actors-map.js оновлено успішно! Збережено записів: {len(actors_map)}")