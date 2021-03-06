from pygments.token import Token

TOKENS = [
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "template"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n  "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "table"),
    (Token.Text, " "),
    (Token.Name.Attribute, "class"),
    (Token.Operator, "="),
    (Token.Literal.String, '"table table-hover"'),
    (Token.Punctuation, ">"),
    (Token.Text, "\n    "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "thead"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n      "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "tr"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n        "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "th"),
    (Token.Text, " "),
    (Token.Name.Attribute, "scope"),
    (Token.Operator, "="),
    (Token.Literal.String, '"col"'),
    (Token.Punctuation, ">"),
    (Token.Name.Other, "Title"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "th"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n        "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "th"),
    (Token.Text, " "),
    (Token.Name.Attribute, "scope"),
    (Token.Operator, "="),
    (Token.Literal.String, '"col"'),
    (Token.Punctuation, ">"),
    (Token.Name.Other, "Author"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "th"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n        "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "th"),
    (Token.Text, " "),
    (Token.Name.Attribute, "scope"),
    (Token.Operator, "="),
    (Token.Literal.String, '"col"'),
    (Token.Punctuation, ">"),
    (Token.Name.Other, "Read"),
    (Token.Operator, "?"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "th"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n        "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "th"),
    (Token.Text, " "),
    (Token.Name.Attribute, "scope"),
    (Token.Operator, "="),
    (Token.Literal.String, '"col"'),
    (Token.Punctuation, ">"),
    (Token.Name.Other, "Purchase"),
    (Token.Text, " "),
    (Token.Name.Other, "Price"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "th"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n        "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "th"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "th"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n      "),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "tr"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n    "),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "thead"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n    "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "tbody"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n      "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "tr"),
    (Token.Text, " "),
    (Token.Name.Tag, "v-for"),
    (Token.Literal.String, '="(book, index) in books" '),
    (Token.Name.Tag, ":key"),
    (Token.Literal.String, '="index"'),
    (Token.Punctuation, ">"),
    (Token.Text, "\n        "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "td"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, "{"),
    (Token.Punctuation, "{"),
    (Token.Text, " "),
    (Token.Name.Other, "book"),
    (Token.Punctuation, "."),
    (Token.Name.Other, "title"),
    (Token.Text, " "),
    (Token.Punctuation, "}"),
    (Token.Punctuation, "}"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "td"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n        "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "td"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, "{"),
    (Token.Punctuation, "{"),
    (Token.Text, " "),
    (Token.Name.Other, "book"),
    (Token.Punctuation, "."),
    (Token.Name.Other, "author"),
    (Token.Text, " "),
    (Token.Punctuation, "}"),
    (Token.Punctuation, "}"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "td"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n        "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "td"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n          "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "span"),
    (Token.Text, " "),
    (Token.Name.Tag, "v-if"),
    (Token.Literal.String, '="book.read"'),
    (Token.Punctuation, ">"),
    (Token.Name.Attribute, "Yes"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "span"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n          "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "span"),
    (Token.Text, " "),
    (Token.Name.Tag, "v-else"),
    (Token.Punctuation, ">"),
    (Token.Name.Attribute, "No"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "span"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n        "),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "td"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n        "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "td"),
    (Token.Punctuation, ">"),
    (Token.Name.Other, "$"),
    (Token.Punctuation, "{"),
    (Token.Punctuation, "{"),
    (Token.Text, " "),
    (Token.Name.Other, "book"),
    (Token.Punctuation, "."),
    (Token.Name.Other, "price"),
    (Token.Text, " "),
    (Token.Punctuation, "}"),
    (Token.Punctuation, "}"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "td"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n        "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "td"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n          "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "button"),
    (Token.Text, " "),
    (Token.Name.Attribute, "type"),
    (Token.Operator, "="),
    (Token.Literal.String, '"button"'),
    (Token.Text, "\n                  "),
    (Token.Name.Attribute, "class"),
    (Token.Operator, "="),
    (Token.Literal.String, '"btn btn-warning btn-sm"'),
    (Token.Text, "\n                  "),
    (Token.Name.Tag, "v-b-modal.book-update-modal"),
    (Token.Text, "\n                  "),
    (Token.Name.Tag, "@click"),
    (Token.Literal.String, '="editBook(book)"'),
    (Token.Punctuation, ">"),
    (Token.Text, "\n              "),
    (Token.Name.Attribute, "Update"),
    (Token.Text, "\n          "),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "button"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n          "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "button"),
    (Token.Text, " "),
    (Token.Name.Attribute, "type"),
    (Token.Operator, "="),
    (Token.Literal.String, '"button"'),
    (Token.Text, "\n                  "),
    (Token.Name.Attribute, "class"),
    (Token.Operator, "="),
    (Token.Literal.String, '"btn btn-danger btn-sm"'),
    (Token.Text, "\n                  "),
    (Token.Name.Tag, "@click"),
    (Token.Literal.String, '="onDeleteBook(book)"'),
    (Token.Punctuation, ">"),
    (Token.Text, "\n              "),
    (Token.Name.Attribute, "Delete"),
    (Token.Text, "\n          "),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "button"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n        "),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "td"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n      "),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "tr"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n    "),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "tbody"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n  "),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "table"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "template"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n"),
]
