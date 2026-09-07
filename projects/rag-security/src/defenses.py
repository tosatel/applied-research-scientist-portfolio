from retrieval import rank_documents
def retrieve(q,docs,condition,k=3,alpha=.65,threshold=.55):
    if condition=="clean_rag": return rank_documents(q,[d for d in docs if int(d["is_trusted"])==1],"relevance",k,alpha,threshold)
    if condition=="poisoned_rag": return rank_documents(q,docs,"relevance",k,alpha,threshold)
    if condition=="naive_defense": return rank_documents(q,docs,"threshold",k,alpha,threshold)
    if condition=="trust_aware_rag": return rank_documents(q,docs,"trust_aware",k,alpha,threshold)
    raise ValueError(condition)
