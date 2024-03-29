/****************************************************************************
 * fifteen.c
 *
 * Fulltime Programmeren 1
 * Robin Laponder
 *
 * Implements Game of Fifteen (generalized to d x d).
 ***************************************************************************/

#define _XOPEN_SOURCE 500

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// Constants
#define DIM_MIN 3
#define DIM_MAX 9
#define COLOR "\033[32m"

// Board
int board[DIM_MAX][DIM_MAX];

// Dimensions
int d;

// Prototypes
void clear(void);
void greet(void);
void init(void);
void draw(void);
bool move(int tile);
bool won(void);

int main(int argc, string argv[])
{
    // Ensure proper usage
    if (argc != 2)
    {
        printf("Usage: fifteen d\n");
        return 1;
    }

    // Ensure valid dimensions
    d = atoi(argv[1]);
    if (d < DIM_MIN || d > DIM_MAX)
    {
        printf("Board must be between %i x %i and %i x %i, inclusive.\n",
               DIM_MIN, DIM_MIN, DIM_MAX, DIM_MAX);
        return 2;
    }

    // Open log
    FILE *file = fopen("log.txt", "w");
    if (file == NULL)
    {
        return 3;
    }

    // Greet user with instructions
    greet();

    // Initialize the board
    init();

    // Accept moves until game is won
    while (true)
    {
        // Clear the screen
        clear();

        // Draw the current state of the board
        draw();

        // Log the current state of the board (for testing)
        for (int i = 0; i < d; i++)
        {
            for (int j = 0; j < d; j++)
            {
                fprintf(file, "%i", board[i][j]);
                if (j < d - 1)
                {
                    fprintf(file, "|");
                }
            }
            fprintf(file, "\n");
        }
        fflush(file);

        // Check for win
        if (won())
        {
            printf("\x1b[32mftw!\n");
            break;
        }

        // Prompt for move
        int tile = get_int("\x1b[00mTile to move: ");

        // Quit if user inputs 0 (for testing)
        if (tile == 0)
        {
            break;
        }

        // Log move (for testing)
        fprintf(file, "%i\n", tile);
        fflush(file);

        // Move if possible, else report illegality
        if (!move(tile))
        {
            printf("\nIllegal move.\n");
            usleep(500000);
        }

        // Sleep thread for animation's sake
        usleep(50000);
    }

    // Close log
    fclose(file);

    // Success
    return 0;
}

// Clears screen using ANSI escape sequences
void clear(void)
{
    printf("\033[2J");
    printf("\033[%d;%dH", 0, 0);
}

// Greets player
void greet(void)
{
    clear();
    printf("\x1b[39mWELCOME TO GAME OF FIFTEEN\n\n");
    usleep(2000000);
}

// Initializes the game's board with tiles numbered 1 through d*d - 1
// (i.e., fills 2D array with values but does not actually print them)
void init(void)
{
    // set the variable for the decrementation of the tiles
    int k = 1;

    // iterate over the rows
    for (int i = 0; i < d; i++)
    {
        // iterate over the columns and set the value of the tiles
        for (int j = 0; j < d; j++, k++)
        {
            board[i][j] = (d * d - k);
        }
    }

    // swap 1 and 2 of the number of tiles on the board is even
    if ((d * d) % 2 == 0)
    {
        board[d - 1][d - 3] = 1;
        board[d - 1][d - 2] = 2;
    }
}

// Prints the board in its current state
void draw(void)
{
    // iterate over the rows
    for (int i = 0; i < d; i++)
    {
        // iterate over the columns and print the tiles
        for (int j = 0; j < d; j++)
        {
            // change the tile with 0 to an underscore
            if (board[i][j] == 0)
            {
                printf("\x1b[44;34m _ ");
                printf("\x1b[49m  ");
            }
            else
            {
                printf("\x1b[34;49m%2i   ", board[i][j]);
            }
        }
        printf("\n\n");
    }
}

// If tile borders empty space, moves tile and returns true, else returns false
bool move(int tile)
{
    // only accept tiles that are on the board
    if (tile <= 0 || tile >= d * d)
    {
        return false;
    }

    // search for the position of the tile
    int row = 0, column = 0;
    for (int i = 0; i < d; i++)
    {
        for (int j = 0; j < d; j++)
        {
            if (tile == board[i][j])
            {
                row = i;
                column = j;
            }
        }
    }

    // check if the tile can be moved and if yes, move it
    if (row - 1 >= 0 && board[row - 1][column] == 0)
    {
        board[row - 1][column] = board[row][column];
        board[row][column] = 0;
        return true;
    }
    else if (row + 1 < d && board[row + 1][column] == 0)
    {
        board[row + 1][column] = board[row][column];
        board[row][column] = 0;
        return true;
    }
    else if (column - 1 >= 0 && board[row][column - 1] == 0)
    {
        board[row][column - 1] = board[row][column];
        board[row][column] = 0;
        return true;
    }
    else if (column + 1 < d && board[row][column + 1] == 0)
    {
        board[row][column + 1] = board[row][column];
        board[row][column] = 0;
        return true;
    }

    // return false if the tile cannot be moved
    else
    {
        return false;
    }
}

// Returns true if game is won (i.e., board is in winning configuration), else false
bool won(void)
{
    // iterate over the rows and column to check the order of the tiles
    int k = 0;
    for (int i = 0; i < d; i++)
    {
        for (int j = 0; j < d; j++)
        {
            // return false if a tile is not in the right place
            if (++k != (d * d) && k != board[i][j])
            {
                return false;
            }
        }
    }

    // all tiles are correct, so return true
    return true;
}
