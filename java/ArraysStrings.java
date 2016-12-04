/**
 * Java programming examples with arrays and strings
**/


import java.util.Arrays;
import java.util.HashMap;


class ArraysStrings {

    public static boolean hasAllUniqueChars(String string) {
	/** return true if string has all unique characters, false
	 * otherwise. 
	 **/

	// assume 7-bit ASCII characters
	
	// there are only 128 unique characters..
	if (string.length() > 128) {
	    return false;
	}
	boolean[] seen = new boolean[128];
	for (int i=0; i < string.length(); i++) {
	    int code = string.charAt(i);
	    if (seen[code]) {
		// character has been seen before
		return false;
	    }
	    seen[code]= true;
	}
	return true;
    }

    public static boolean hasAllUniqueChars2(String string) {
	/** return true if string has all unique characters, false
	 * otherwise. no additional data structure is being allowed
	 **/
	char[] chars = string.toCharArray();
	Arrays.sort(chars);
	for (int i=0; i < chars.length-1; i++) {
	    if (chars[i] == chars[i+1]) {
		return false;
	    }
	}
	return true;
    }

    public static boolean checkPermutation(String string1, String string2) {
	/** return true if string1 is a permutation of string2, false
	 * otherwise
	 **/
	// if strings are of different lenght, return false
	if (string1.length() != string2.length()) {
	    return false;
	}
	// assume 7-bit ASCII
	// assume whitespace matters and problem is case sensitive

	// to be permutaitons strings must have the same characters
	// use a arary to count characters in string1
	int[] counts = new int[128];
	for (char c : string1.toCharArray()) {
	    counts[(int)c] += 1;
	}
	//decrement counts for characters in string2, if we hit a
	//negative number return false
	for (char c : string2.toCharArray()) {
	    counts[(int)c] -= 1;
	    if (counts[(int)c] < 0) {
		return false;
	    }
	}
	// as both strings have same lenght there can be no more
	// positive counts
	return true;
    }


    public static void main(String[] args) {
	// 1.1 has all unqiue characters
	System.out.println("hasAllUniqueChars('foo') = " + hasAllUniqueChars("foo"));
	System.out.println("hasAllUniqueChars('bar') = " + hasAllUniqueChars("bar"));

	System.out.println("hasAllUniqueChars2('foo') = " + hasAllUniqueChars2("foo"));
	System.out.println("hasAllUniqueChars2('bar') = " + hasAllUniqueChars2("bar"));
	
	// 1.2 check if string is permutation
	System.out.println("checkPermutation('bar', 'ba') = " + checkPermutation("bar", "ba"));
	System.out.println("checkPermutation('bar', 'bat') = " + checkPermutation("bar", "bat"));
	System.out.println("checkPermutation('bar', 'rab') = " + checkPermutation("bar", "rab"));
    }
}
