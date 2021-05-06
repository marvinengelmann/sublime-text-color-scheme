import json

data = {
    "name": "fuck",
    "globals": {
        "background": "#000000",
        "foreground": "#ffffff",
        "selection": "#000000",
        "selection_border": "#ffffff",
        "caret": "#00ff00",
    },
    "rules": [
        {
            "name": "Pale Green",
            "foreground": "#98fb98",
            "scope": ", ".join([
                "constant.numeric",
                "constant.other.color"
            ])
        },
        {
            "name": "Lime",
            "foreground": "#00ff00",
            "scope": ", ".join([
                "keyword",
                "punctuation.definition.numeric",
                "punctuation.separator.combinator",
                "entity.other.pseudo-class",
                "entity.other.pseudo-element",
                "storage.type.function.arrow",
                "storage.type.numeric",
                "storage.modifier.reference",
                "constant.other.placeholder",
                "constant.character.escape"
            ])
        },
        {
            "name": "Light Green",
            "foreground": "#90ee90",
            "scope": ", ".join([
                "constant.language",
                "support.type",
                "support.class",
                "support.other.namespace",
                "entity.name.class",
                "entity.other.inherited-class",
                "entity.name.interface",
                "entity.name.trait",
                "entity.name.namespace",
                "entity.name.struct",
                "entity.name.enum",
                "entity.name.type",
                "variable.type",
                "storage.type.source"
            ])
        },
        {
            "name": "Green Yellow",
            "foreground": "#adff2f",
            "scope": ", ".join([
                "storage.type",
                "storage.modifier",
                "variable.language",
                "entity.name.tag",
                "support.type.primitive"
            ])
        },
        {
            "name": "Medium Spring Green",
            "foreground": "#00fa9a",
            "scope": ", ".join([
                "variable.function",
                "variable.annotation",
                "entity.name.function",
                "entity.other.attribute-name",
                "support.function",
                "support.macro"
            ])
        },
        {
            "name": "Aquamarine",
            "foreground": "#7fffd4",
            "scope": ", ".join([
                "string"
            ])
        },
        {
            "name": "Dark Slate Gray",
            "foreground": "#2f4f4f",
            "scope": ", ".join([
                "comment",
                "punctuation.definition.comment"
            ])
        },
        {
            "name": "White",
            "foreground": "#ffffff",
            "scope": ", ".join([
                "variable",
                "punctuation",
                "keyword.operator.type.annotation"
            ])
        },
        {
            "name": "Italic",
            "scope": ", ".join([
                "constant.language",
                "keyword",
                "keyword.operator.word",
                "storage.type",
                "storage.modifier",
                "variable.language",
                "entity.name.tag",
                "entity.other.pseudo-class",
                "entity.other.pseudo-element",
                "support.type.primitive"
            ]),
            "font_style": "italic"
        },
        {
            "name": "None",
            "scope": ", ".join([
                "keyword.operator",
                "keyword.other.unit",
                "keyword.declaration.doctype",
                "storage.type.function.arrow",
                "storage.type.source",
                "storage.modifier.reference",
                "entity.name.tag.html",
                "entity.name.tag.",
                "constant.language.doctype"
            ]),
            "font_style": ""
        }
    ]
}

with open('fuck.sublime-color-scheme', 'w') as outfile:
    json.dump(data, outfile, indent=4)