from pathlib import Path
import plistlib

import yaml
from jinja2 import Template

IN_PATH = Path(__file__).parent.joinpath("myst.tmLanguage.yaml.j2")
LANGUAGE_PATH = Path(__file__).parent.joinpath("languages.yaml")
DIRECTIVE_PATH = Path(__file__).parent.joinpath("directives.yaml")
OUT_PATH = Path(__file__).parent.joinpath("../syntaxes/myst.tmLanguage")

if __name__ == "__main__":

    # read variables
    directives = yaml.safe_load(DIRECTIVE_PATH.read_text("utf8"))
    languages = yaml.safe_load(LANGUAGE_PATH.read_text("utf8"))

    # inject variables
    template_yaml = IN_PATH.read_text("utf8")
    template = Template(template_yaml)
    input_yaml = template.render(
        admonition_classes=directives["admonition_classes"],
        code_classes=directives["code_classes"],
        languages=languages,
    )

    # dump to plist
    data = yaml.safe_load(input_yaml)
    plist_string = plistlib.dumps(data, sort_keys=False)
    OUT_PATH.write_bytes(plist_string)
