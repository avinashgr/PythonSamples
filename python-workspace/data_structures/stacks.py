#define a stack of books
books  = ['Dune Messiah', 'The Shining', '2001: A Space Odessey', 'A Brief History Of Time']
#notice here that the last book is at the top of the stack
#get book at the stop of the stack
print(f'the book at top of stack is "{books.pop()}"')
# print the stack after popping
print(f'the stack of books now is {books}')
