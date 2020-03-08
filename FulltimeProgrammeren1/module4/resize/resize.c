/****************************************************************************
 * resize.c
 *
 * Fulltime Programmeren 1
 * Robin Laponder
 *
 * Copies and resizes a BMP file.
 ***************************************************************************/

#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage part 1
    if (argc != 4)
    {
        printf("Usage: ./resize n infile outfile\n");
        return 1;
    }

    // convert entered number to an integer, ensure proper usage part 2
    int factor = atoi(argv[1]);
    if (factor < 0 || factor > 100)
    {
        printf("Entered number must be a positive integer less than or equal to 100.\n");
        return 1;
    }

    // remember filenames
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    // convert old dimensions to new dimensions
    int width_old = bi.biWidth;
    int height_old = bi.biHeight;
    int width_new = bi.biWidth * factor;
    int height_new = bi.biHeight * factor;

    // calculate the padding for input and output
    int padding_old = (4 - (width_old * sizeof(RGBTRIPLE)) % 4) % 4;
    int padding_new = (4 - (width_new * sizeof(RGBTRIPLE)) % 4) % 4;

    // update header in output
    bi.biWidth = width_new;
    bi.biHeight = height_new;
    bi.biSizeImage = ((sizeof(RGBTRIPLE) * width_new) + padding_new) * abs(height_new);
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(height_old); i < biHeight; i++)
    {
        // declare scanline
        RGBTRIPLE scanline[width_new * sizeof(RGBTRIPLE)];

        // iterate over pixels in infile's scanlines
        for (int j = 0; j < width_old; j++)
        {
            // temporary storage
            RGBTRIPLE triple;

            // read RGB triple from infile
            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

            // copy pixels horizontally
            for (int k = 0; k < factor; k++)
            {
                scanline[(j * factor) + k] = triple;
            }
        }

        // skip over padding, if any
        fseek(inptr, padding_old, SEEK_CUR);

        // copy pixels vertically
        for (int j = 0; j < factor; j++)
        {
            // write the pixels in the scanline
            fwrite(scanline, sizeof(RGBTRIPLE), width_new, outptr);

            // write the new padding
            for (int k = 0; k < padding_new; k++)
            {
                fputc(0x00, outptr);
            }
        }
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}