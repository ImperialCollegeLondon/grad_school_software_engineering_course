---
title: "Writing unit tests"
teaching: 40
exercises: 60
questions:
- "What is a unit test?"
- "How do I write and run unit tests"
- "How can I avoid test duplication and ensure isolation?"
- "How can I run tests automatically and measure their coverage?"
objectives:
 - "Implement effective unit tests using pytest"
 - "Execute tests in Visual Studio Code"
 - "Explain the issues relating to non-deterministic code"
 - "Implement mocking, fixtures and test parametrisation using pytest decorators"
 - "Configure git hooks and pytest-coverage"
 - "Apply best-practices when setting up a new Python project"
 - "Recognise analogous tools for other programming languages"
 - "Apply testing to Jupyter notebooks"
keypoints:
 - "Python has a built-in testing framework, but pytest is not only more extensible, it's also more concise even for the simplest case"
 - "Testing with VS Code is fairly frictionless and encourages good habits (writing tests as you code, test-driven development)"
 - "Seeding random number generators and adding tolerances can help to test non-deterministic code (though presents challenges)"
 - "Important to have a set-up you can use for every project - so that it becomes as routine in your workflow as version control itself"
 - "git bisect is a cool way to identify when a test broke (retrospectively)"
 - "git hooks provide a way to automate testing (and other QA processes)"
 - "pytest has a myriad of extensions that are worthy of mention, if not demonstrating, such as Jupyter, benchmark, Hypothesis, tox etc"
 - "Testing is not only standard practice in mainstream software engineering, it also provides distinct benefits for any non-trivial research software"
 - "Demonstrate adding a test case to a basic scientific code. Exercise involves adding others (see below)."
 - "Demonstrate how to create a repo from our GitHub template repository - and how the tests are run automatically and immediately on any change to your copy of the code"
 - "Brief demonstration jupyter-ci"
---

{% include links.md %}
