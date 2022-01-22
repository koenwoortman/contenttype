# Parse Content-Type Headers
> Python package for parsing Content-Type HTTP headers

[![PyPI](https://img.shields.io/pypi/v/check-rq?color=blue)](https://pypi.org/project/check-rq/)

## Usage

```python
from contenttype import ContentType

result = ContentType.parse('application/rss+xml; charset=utf-8')

result.type       # => 'application'
result.subtype    # => 'rss'
result.suffix     # => 'xml'
result.parameters # => {'charset': 'utf-8'}
result.charset    # => 'utf-8'
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
