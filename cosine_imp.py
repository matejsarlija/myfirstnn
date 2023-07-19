v1 = [0,3,4,5,6]
v2 = [4,5,6,7,8]

def dot(v1, v2):
    dot_product = sum((a * b) for a, b in zip(v1, v2))
    return dot_product

def cosine_similarity(v1, v2):
    '''
    (v1 dot v2) / ||v1||* ||v2||
    '''
    products = dot(v1, v2)
    denominator = ((dot(v1, v1) ** .5) * (dot(v2, v2) ** .5))
    similarity = products / denominator
    return similarity

print(cosine_similarity(v1, v2))
