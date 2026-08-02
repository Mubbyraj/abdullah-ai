from services.knowledge_loader import load_all_sources
from services.vector_engine import create_vector_index


documents = load_all_sources()


print(f"Documents loaded: {len(documents)}")


index, model = create_vector_index(documents)



def search_knowledge(query, top_k=3):

    results = index.search(
        query,
        top_k
    )


    return results