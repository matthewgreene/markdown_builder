# markdown_builder

Simple Python package for creating Markdown documents in code.

## Currently supported Markdown Elements (more to come!)

- Headers
- Lists
   - Checkbox
   - Ordered
   - Unordered
- Tables
- Paragraphs
- Links


## Examples
To start building Markdown documents in code, we must first create a `MarkdownBuilder` instance.

```python
md = MarkdownBuilder()
```

This serves as the entrypoint for all Markdown elements to be added to the document. From here we begin adding new elements.

### Headers
```python
md.addHeader(level=1, text="Test Header")
```
The above command will generate to following syntax:

```markdown
# Test Header
``` 

### Lists

```python
md = MarkdownBuilder()
uol = UnorderedList(["one", "two", UnorderedList(["four", "five"]), "three"])
md.addList(uol)
```