# import numpy as np

# def cosine_similarity(a: list, b: list) -> float:
#     """
#     Returns the cosine similarity as a Python float.
#     """
#     # Write code here
#     for i,j in zip(a,b):
#         dot_pro+=i*j
#         a_squre+=i*i
#         b_squre+=j*j

#     if a_squre==0.0 or b_squre==0.0:
#         return 0.0

#     norm_a=math.squrt(a_squre)
#     norm_b=math.squrt(b_squre)
#     return float(dot_pro/(norm_a*norm_b))
import numpy as np


def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    vec_a = np.asarray(a, dtype=np.float64)
    vec_b = np.asarray(b, dtype=np.float64)

    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)

    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0

    dot_product = np.dot(vec_a, vec_b)
    return float(dot_product / (norm_a * norm_b))