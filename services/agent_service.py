from helper_methods import get_embeddings, search_qdrant, filter_chunks, generate_agent_response
from schemas import chat_response
def build_system_prompt(query: str, context: str):
        return f"""
        You are a professional HR Assistant for an enterprise company.
        Your role is to provide clear, accurate, and helpful responses based strictly on company policies and documents.
        ---------------------
        GUIDELINES:
        ---------------------
        1. Use ONLY the provided context to answer the question.
        2. Do NOT make up information or assume anything beyond the context.
        3. If the answer is not available in the context, respond with:
        "I’m sorry, but I could not find relevant information in the available policies."
        4. Keep the response polite, professional, and helpful.
        5. Answer in a clear and concise paragraph (avoid bullet points unless absolutely necessary).
        6. Do not mention "context" or "document" in your response.
        7. If possible, slightly rephrase and summarize instead of copying text directly.
        8. Maintain a human conversational tone (like an HR representative).
        ---------------------
        CONTEXT:
        {context}
        ---------------------
        USER QUESTION:
        {query}
        ---------------------
        FINAL ANSWER:
        """

async def get_agent_response(message: str) -> chat_response:
        query_emb = get_embeddings(message)
        searched_val = search_qdrant(query_emb, 101)
        best_chunks = filter_chunks(searched_val)
        if not best_chunks:
                return chat_response(response="No relevant data found!")
        context = "\n".join(
                chunk.payload.get("content", "")
                for chunk in best_chunks
                if isinstance(getattr(chunk, "payload", None), dict)
        )
        if not context.strip():
                return chat_response(response="No relevant data found!")
        prompt = build_system_prompt(message, context)
        agent_response = generate_agent_response(prompt)
        return chat_response(response=agent_response)


