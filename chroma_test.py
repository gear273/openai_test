import chromadb
from chromadb.config import Settings

client = chromadb.Client()

client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory=".chromadb" # Optional, defaults to .chromadb/ in the current directory
))

# collection = client.create_collection("sample_collection")
collection = client.get_collection("sample_collection")

# Add docs to the collection. Can also update and delete. Row-based API coming soon!
# documents = [
#     "Recipe1: Add 200g of flour and mix with 100g of sugar. Add 2 eggs and stir until smooth.",
#     "Recipe2: Blend 2 bananas with 1 cup of milk and a spoonful of honey for a healthy smoothie.",
#     "Recipe3: Boil 500g of potatoes for 20 minutes, then mash them and add butter and salt to taste.",
#     "Recipe4: Fry a chopped onion, add 400g of diced chicken and cook until done. Add curry sauce and simmer for 15 minutes.",
#     "Recipe5: Preheat the oven to 180C. Mix 250g of pasta with cheese and tomato sauce, then bake for 20 minutes.",
#     "Recipe6: Mix 200g of ground beef with breadcrumbs and an egg. Shape into patties and grill for 15 minutes.",
#     "Recipe7: Boil 1 cup of rice in 2 cups of water until done. Fry with vegetables and soy sauce for a quick stir fry.",
#     "Recipe8: Spread butter on two slices of bread. Add ham, cheese, lettuce, and tomato for a classic sandwich.",
#     "Recipe9: Preheat oven to 200C. Roll out a pizza dough, spread with tomato sauce, sprinkle cheese and bake until golden brown.",
#     "Recipe10: Cut a loaf of bread into slices. Drizzle with olive oil and rub with garlic for a simple garlic bread.",
# ]
# metadatas = [
#     {"source": "notion"},
#     {"source": "google-docs"},
#     {"source": "my-recipes"},
#     {"source": "chef-john"},
#     {"source": "granny-recipes"},
#     {"source": "vegan-life"},
#     {"source": "daily-cookbook"},
#     {"source": "home-chef"},
#     {"source": "mamma-mia"},
#     {"source": "culinary-corner"}
# ]
# ids = ["recipe1", "recipe2", "recipe3", "recipe4", "recipe5", "recipe6", "recipe7", "recipe8", "recipe9", "recipe10"]
#
# collection.add(
#     documents=documents,
#     metadatas=metadatas,
#     ids=ids,
# )

results = collection.query(
    query_texts=["Preheat oven to 200C. Roll out a pizza dough, spread with tomato sauce, sprinkle cheese and bake until golden brown."],
    n_results=2,
    # where={"metadata_field": "is_equal_to_this"}, # optional filter
    # where_document={"$contains":"search_string"}  # optional filter
)

print(results)