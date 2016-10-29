/**
 * Implementing a StringBuilder from scratch
**/

import java.util.List;
import java.util.ArrayList;

public class StringBuilder {
    private List<String> strings = new ArrayList<String>();
    private int length = 0;

    public StringBuilder() {
	
    }	
    
    public void append(String string) {
	strings.add(string);
	length += string.length();
    }

    public String toString() {
 	char[] output = new char[length];
	int offset = 0;
	for (String string : strings) {
	    char[] chars = string.toCharArray();
	    for (int i = 0; i < chars.length; i++) {
		output[offset+i] = chars[i];
	    }
	    offset += chars.length;
	}
	return new String(output);
    }

    public static void  main(String[] args) {
	StringBuilder builder = new StringBuilder();
	builder.append("foo");
	builder.append("bar");
	System.out.println(builder.toString());
    }
}
