/****************************************************************************
 * recover.c
 *
 * Fulltime Programmeren 1
 * Robin Laponder
 *
 * Recovers JPEGs from a forensic image.
 ***************************************************************************/

#include <stdio.h>
#include <stdlib.h>

// JPEGs are saved in blocks of 512 bytes
#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover infile\n");
        return 1;
    }

    // remember name infile and open it
    char *infile = argv[1];
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // declare buffer
    unsigned char buffer[BLOCK_SIZE];

    // declare file counter
    int filecount = 0;

    // set pointer to outfiles
    FILE *outptr = NULL;

    // search for JPEGs by reading the data block by block
    while (fread(buffer, BLOCK_SIZE, 1, inptr))
    {
        // search for the first four bytes of a JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // if another JPEG was already found, close it
            if (filecount > 0)
            {
                fclose(outptr);
            }

            // create filename for JPEG
            char filename[8];
            sprintf(filename, "%03i.jpg", filecount);

            // open new JPEG and check if it is created
            outptr = fopen(filename, "w");
            if (outptr == NULL)
            {
                fprintf(stderr, "Could not create %s.\n", filename);
                return 3;
            }

            // increment the number of created files
            filecount++;
        }

        // if a file is created, write the data block by block untill a new JPEG is found
        if (outptr != NULL)
        {
            fwrite(buffer, BLOCK_SIZE, 1, outptr);
        }
    }

    // close the last JPEG and the infile
    fclose(inptr);
    fclose(outptr);

    // succes
    return 0;
}
