from pathlib import Path


def load_documents(folder_path):

    docs = []

    for file in Path(folder_path).glob("*.txt"):

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            docs.append(
                {
                    "source": file.name,
                    "text": f.read()
                }
            )

    return docs