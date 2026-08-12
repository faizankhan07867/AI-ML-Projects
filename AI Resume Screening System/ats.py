skills_database = [

    "python",
    "java",
    "c",
    "c++",
    "sql",
    "mysql",
    "html",
    "css",
    "javascript",
    "react",
    "node",
    "flask",
    "django",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "nlp",
    "opencv",
    "git",
    "github",
    "aws",
    "azure",
    "docker",
    "kubernetes",
    "linux",
    "mongodb"

]


def calculate_score(text):

    found = []

    score = 0

    for skill in skills_database:

        if skill in text:

            found.append(skill)

            score += 4

    if score > 100:

        score = 100

    return score, found