Project BookWorm

# Summary
The subroutine that allows a user to analyze texts and understand how much the author of the text is graphomaniac. The reference measuring system is based on "War and Peace" by Lev Tolstoy

# How it works:
The system counts all unique words and the total amount of words used in the text and divides one to another. The result is the word mediocrity index (always <= 1). This index is compared to Lev Tolstoy's word mediocrity index and the final score is counted. 

# Example: 
If you have a sentence with 8 words: "The man is a wolf to a man" which contains 6 unique words, the index of word mediocrity will be 3/4. Lev Tolstoy's index is: ___, so the author of this line gets "Killed Lev Tolstoy" badge. 

# Precautions:
As you can see from this example, you should keep in mind that the smaller the source text is, the less consistent the estimate would be: one-word text author will always kill Lev Tolstoy +)). To reach the certain level of consistency you need to enter text with at least ____ words which is approximately ____ pages long.

# Additional information:
You can check the grading system in badges.json file under [src\main\resources](https://github.com/shamanengine/BookWorm/blob/master/src/main/resources/badges.json) folder
