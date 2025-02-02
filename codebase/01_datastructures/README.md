# Data Structures

Data structures help organize and store data efficiently in computer memory. They provide a way to manage and manipulate data effectively, enabling faster access, insertion, and deletion operations. Common data structures include linked lists, stacks, queues and trees each serving specific purposes based on the requirements of the problem at hand. Understanding data structures is fundamental for designing efficient algorithms and optimizing software performance.

Table of Contents

- [Data Structures](#data-structures)
  - [1. Stack](#1-stack)
    - [1.2. Adding and removing values from a stack](#12-adding-and-removing-values-from-stack)
    - [1.3. Where is a stack commonly used?](#13-where-is-a-stack-commonly-used?)


## 1. Stack

Stack is a linear data structure that follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out). LIFO implies that the element that is inserted last, comes out first and FILO implies that the element that is inserted first, comes out last.

### 1.2 Adding and removing values from a stack

Push: Adds an element to the top of the stack.

Pop: Removes and returns the top element of the stack.

Imagine a pile of books on the floor on a spring-loaded device so that the top of the stack stays nearly the same height. When we add a book to the stack, we say that we 'push' it onto the stack, and when we remove a book, we say that we 'pop' it from the stack.

### 1.3 Where is a stack commonly used?

1. Expression Evaluation and Conversion
   
  - Infix to Postfix/Prefix Conversion: Stacks are used to convert infix expressions (e.g., a + b) to postfix (ab+) or prefix (+ab) for easier evaluation by computers.
  - Postfix Evaluation: Stacks simplify evaluating postfix expressions like 23+ to give results.

2. Function Call Management (Recursion)
   
   - The system stack is used to manage function calls. When a function is called, its data (e.g., local variables) is pushed onto the stack. When the function completes, the data is popped off.
  
3. Browser Navigation
   
   - Browsers use stacks to manage the history of web pages:
     - Back Button: Pops the current page from the stack to go to the previous page.
     - Forward Button: Uses another stack to store forward navigation.
