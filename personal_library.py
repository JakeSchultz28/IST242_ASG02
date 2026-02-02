"""
Simple Personal Library
Author: Jacob Schultz
Version: v1
"""

def show_menu():
    """
    Display the main menu.
    """

    print('\nPersonal Library Menu:\n'
          '----------------------\n'
          '1. Add a Book\n'
          '2. Remove a Book\n'
          '3. List All Books\n'
          '4. Search Books\n'
          '5. Exit\n')


def add_book(library: list[str]):
    """
    Add a book to the library.
    
    :param library: list of all books
    :type library: list[str]
    """

    add_another = 'y'
    while add_another.upper() == 'Y':
        # Prompt user for a book title to add
        new_book = input('\nEnter the title of a book to add: ')
        # Add the book to the library
        library.append(new_book)
        # Echo print to confirm that the book was added
        print(f'"{new_book}" has been added.')
        # Ask user if they want to add another book
        add_another = input('\nWould you like to add another book? (Y/N): ')
        
    return library


def remove_book(library: list[str]):
    """
    Remove a book from the library.
    
    :param library: list of all books
    :type library: list[str]
    """
    
    while True:
        # Prompt the user for a book to remove
        book = input('\nEnter the title of a book to remove (0 to quit): ')

        # Remove the book from the library
        if book in library:
            library.remove(book)
            print(f'"{book}" has been removed from the library.')
            input('\nPress Enter to return to menu...')
            break
        # Quit to menu
        elif book == '0':
            break
        # Tell the user their book was not found and could not be removed
        else:
            print(f'"{book}" was not found. Please try again.')

    return library


def list_books(library: list[str]):
    """
    List all of the books in the library.
    
    :param library: list of all books
    :type library: list[str]
    """

    print('\nAll Books:')
    print('----------')

    # Print the library list line by line
    for item in library:
        print(item)
    input('\nPress Enter to return to menu...')


def search_books(library: list[str]):
    """
    Search the library list and output all matches.
    
    :param library: list of all books
    :type library: list[str]
    """

    # Measures how many results were found
    result_counter = 0

    # Prompt user for search criteria
    user_search = input('\nEnter a partial or full title to search: ')
    print('\nResults:')
    print('--------')
    # Iterate over all items in the library
    for item in library:
        # Print any item that contains the searched string
        if user_search in item:
            print(item)
            result_counter += 1
    # If no results were printed, tell the user
    if result_counter == 0:
        print(f'No results found for "{user_search}"...')
    input('\nPress Enter to return to menu...')


def main():
    """
    Main logic.
    """

    library: list[str] = []
    while True:
        # Print the main menu
        show_menu()
        # Prompt the user for a menu option and execute that function
        menu_choice = input('Please select your option (1-5): ')
        if menu_choice == '1':
            add_book(library)
        elif menu_choice == '2':
            remove_book(library)
        elif menu_choice == '3':
            list_books(library)
        elif menu_choice == '4':
            search_books(library)
        elif menu_choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid input. Please enter a number between 1 and 5')


if __name__ == "__main__":
    main()