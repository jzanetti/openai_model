from os.path import join
from os import getenv
import openai
from process import MODEL



def sg(txt: str, max_tokens=30) -> str:

    openai.api_key = getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model=MODEL,
        prompt=f"Correct this to standard English:\n\n{txt}",
        temperature=0,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text


def write_output(workdir: str, txt: str):
    output_path = join(workdir, "sg_output.txt")
    with open(output_path, "w") as fid:
        fid.write(txt)