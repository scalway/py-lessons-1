# Contributing to Python Lessons

Thank you for your interest in contributing to this Python lessons repository! This document provides guidelines for contributing.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. Check if the issue already exists in the [Issues](https://github.com/scalway/py-lessons-1/issues) section
2. If not, create a new issue with a clear title and description
3. Include code examples if applicable
4. Specify which lesson the issue relates to

### Adding New Lessons

If you'd like to add a new lesson:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/new-lesson-name`
3. Follow the lesson structure:
   ```
   lessons/XX_lesson_name/
   ├── README.md        # Lesson overview and learning objectives
   ├── examples.py      # Working code examples
   └── exercises.py     # (Optional) Practice exercises
   ```
4. Ensure your code follows PEP 8 style guidelines
5. Test your examples thoroughly
6. Update the main README.md to include your lesson
7. Submit a pull request

### Improving Existing Lessons

To improve existing lessons:

1. Fork the repository
2. Create a new branch: `git checkout -b improve/lesson-name`
3. Make your changes
4. Ensure all examples still work
5. Submit a pull request with a clear description of improvements

## Code Style Guidelines

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Include docstrings for functions and classes
- Add comments for complex logic
- Keep examples simple and focused

## Example Code Requirements

All example code should:

- Be self-contained and runnable
- Include clear output or demonstrations
- Handle errors gracefully
- Be well-commented
- Follow best practices

## Testing

Before submitting:

1. Test all your examples: `python examples.py`
2. Run the test suite: `python test_all.py`
3. Ensure no errors or warnings

## Documentation

- Each lesson needs a README.md with:
  - Learning objectives
  - Topics covered
  - How to run examples
  - Key concepts
- Use clear, beginner-friendly language
- Include code examples in documentation

## Pull Request Process

1. Update the README.md if needed
2. Ensure your code passes all tests
3. Update requirements.txt if you add dependencies
4. Provide a clear PR description
5. Link any related issues

## Questions?

Feel free to open an issue for any questions about contributing!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
