---
title: "Testing Overview"
teaching: 15
exercises: 5
questions:
- "Why test my software?"
- "How can I test my software?"
- "How much testing is 'enough'?"
objectives:
- "Appreciate the benefits of testing research software"
- "Understand what testing can and can't achieve"
- "Describe various approaches to testing, and relevant trade-offs"
- "Understand the concept of test coverage, and how it relates to software quality and sustainability"
- "Appreciate the benefits of test automation"
keypoints:
- "Testing is the standard approach to software quality assurance"
- "Testing ensures that code performs its intended function"
- "Code without any tests should arouse suspicion, but it is entirely possible to write a comprehensive but practically worthless test suite"
- "Good tests thoroughly exercise critical code"
- "Well-tested code is likely to be more reliable, correct and malleable."
- "Testing can also contribute to performance, security and long-term stability as the size of the codebase and its network of contributors grows"
- "It can also be use to ensure that software has been installed correctly, is portable to new platforms, is compatible with new versions of its dependencies..."
- "In the context of research software, testing can be used to validate code i.e. ensure that it faithfully implements scientific theory - with some caveats"
- "Types of testing and the kinds of bugs they can help to avoid: Unit, e.g. a function; Functional, e.g. a library; Regression, e.g. a bug"
- "Test coverage can provide a coarse- or fine-grained metric of comprehensiveness, if not quality. But typically does provide another signal of code quality."
- "Automated tests (and coverage calculation) is another such signal: Lowers friction; Ensures that breakage is identified sooner, and isn't released; Implies that machine-readable instructions exist for building and code and running the tests"
- "Testing ultimately contributes to sustainability i.e. that software is, and remains, fit for purpose as its functionality and/or contributor-base grows, and its dependencies and/or runtime environments change"
---

### Why Test?

We test software to ensure that it is (and remains) fit for purpose.

In the context of research software typically we want to validate that it correctly
encodes physical laws or mathematical relationships, but there are many other reasons:

* Check that code works when running on a new system
* Make sure new code changes do not break existing functionality
* Ensure code correctly handles edge or corner cases
* Persuade others your code is reliable
* Check that code works with new or updated dependencies

Whilst testing might seem like an intimidating topic the chances are you're
already doing testing in some form. No matter the level of experience, no
programmer ever just sits down and writes some code, is perfectly confident that
sit works and proceeds to use it straight away in research. Instead development
is in practice more piecemeal - you generally think about a simple input and the
expected output then write some simple code that works. Then, iteratively, you
think about more complicated example inputs and outputs and flesh out the code
until those work as well.

When developers talk about testing it means formalising the above process to create
a programmatic test suite which makes validation easily repeatable on demand.

This has numerous advantages over a more ad hoc approach:

* Provides a record of the tests that have been carried out
* Faster development times - get feedback on changes quickly
* Encourages writing more modular code
* Ensures breakages are caught early in development
* Prevent manual testing mistakes
* Enables tests to be run automatically e.g. by Continuous Integration systems

As you're performing checks on your code anyway it's worth putting in the time
to formalise your tests and take advantage of the above.

> ## A Hypothetical Scenario
>
> Your supervisor has tasked you with implementing an obscure statistical method
> to use for some data analysis. Wanting to avoid unnecessary work you check
> online to see if an implementation exists. Success! Another researcher has
> already implemented and published the code.
>
> You move to hit the download button, but a worrying thought occurs. How do you
> know this code is right? You don't know the author or his level of programming
> skill. Why should you trust the code?
>
> Now turn this question on its head. Why should your colleagues or supervisor
> trust any implementation of the method that you write? Why should you trust
> work you did a year ago? What about a reviewer for a paper?
>
> This scenario illustrates the sociological value of programmatic testing. If
> published code has tests then you have instant assurance that its authors have
> invested time in the checking the correctness of their code. You can even see
> exactly the tests they've tried and add your own if you're not
> satisfied. Conversely, any code that lacks tests should be viewed with
> suspicion as you have no record of what quality assurance steps have been
> taken.
{: .callout}

### Types of Testing

This isn't a topic we will discuss in much detail but is worth mentioning as the
jargon here can be another factor that is intimidating. In fact there are entire
[websites](http://softwaretestingfundamentals.com) dedicated to explaining the
different types of testing. Ultimately, however there are only a few types of
testing that we need to worry about.

#### Unit Testing

The main type of testing kind we will be dealing with in this course. Unit
testing refers to taking a component of a program and testing it in
isolation. Generally this means testing an individual class or function. This is
part of the reason that testing encourages more modular and sustainable code
development. You're encouraged to write your code into functionally independent
components that can be easily unit tested.

#### Functional Testing

Unlike unit testing that focuses on independent parts of the system, functional
testing checks the compliance of the system overall against a defined set of
criteria. In other words does the software as a whole do what it's supposed to
do?

#### Regression Testing

This refers to the practice of running previously written tests whenever a new
change is introduced to the code, and adding new tests when issues are resolved
to ensure that bugs don't reoccur. This is good to do even when making seemingly
insignificant changes. Carrying out regression testing allows you to remain
confident that your code is functioning as expected even as it grows in
complexity and capability.

### Testing Done Right

It's important to be clear about what software tests are able to provide and
what they are not. Unfortunately it isn't possible to write tests that
completely guarantee that your code is bug free or provides a one hundred
percent faithful implementation of a particular model. In fact it's perfectly
possible to write an impressive looking collection of tests that have very
little value at all. What should be the aim therefore when developing software
tests?

In practice this is difficult to define universally but one useful mantra is
that good tests ***thoroughly exercise critical code***. One way to achieve this
is to design test examples of increasing complexity that cover the most general
case the unit should encounter. Also try to consider examples of special or edge
cases that your function needs to handle especially?

A useful quantitative metric to consider is also test coverage. Using additional
tools it is possible to determine, on a line-by-line basis, which parts a code
are being exercised by its tests. This can be useful to ensure, for instance,
that all logical branching points within the code are being used by the test
inputs.

> ## Testing and Coverage
>
> Consider the following Python function:
>
> ~~~python
> def recursive_fibonacci(n):
>     """Return the nth number of the fibonacci sequence"""
>     if n <= 1:
>         return n
>     else:
>         return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)
> ~~~
>
> Try to think up some test cases of increasing complexity, there are at least four
> distinct cases worth considering. What input value would you use for each case
> and what output value would you expect? Which lines of code will be exercised
> by each test case?
>
> For convenience, some initial terms from the Fibonacci sequence are given
> below:  
> 0, 1, 1, 2, 3, 5, 8, 13, 21
>
> > ## Solution
> >
> > ### Case 1 - Use either 0 or 1 as input
> >
> > **Correct output:** Same as input  
> > **Coverage:** First section of if-block  
> > **Reason:** This represents the simplest possible test for the function. The
> > value of this test is that it exercises only the special case tested for by
> > the if-block.
> >
> > #### Case 2 - Use a value > 1 as input
> >
> > **Correct output:** Appropriate value from the Fibonacci sequence  
> > **Coverage:** All of the code  
> > **Reason:** This is a more fully fledged case that is representative of the
> > majority of the possible range of input values for the function. It covers
> > not only the special case represented by the first if-block but the general
> > case where recursion is invoked.
> >
> > #### Case 3 - Use a negative value as input
> >
> > **Correct output:** Depends...  
> > **Coverage:** First section of if-block  
> > **Reason:** This represents the case of a possible input to the function
> > that is outside of it's intended usage. At the moment the function will just
> > return the input value, but whether this is the correct behaviour depends on
> > the wider context on which it will be used. It might be better for this type
> > of input value to cause an error to be raised however. The value of this
> > test case is that it encourages you to think about this scenario and what
> > the behaviour should be. It also demonstrates to others that you've
> > considered this scenario and the function behaviour is as intended.
> >
> > #### Case 4 - Use a non-integer input e.g. 3.5
> >
> > **Correct output:** Depends...  
> > **Coverage:** Whole function  
> > **Reason:** This is similar to case 3, but may not arise in more strongly
> > typed languages. What should the function do here? Work as is? Raise an
> > error? Round to the nearest integer?
> {: .solution}
{: .challenge}

### Summary

The importance of programmatic testing for software development is difficult to
overstate. As testing on some level is always carried out there is relatively
low cost in formalising the process and much to be gained. The rest of this
course will focus on how to carry out unit testing.

{% include links.md %}
