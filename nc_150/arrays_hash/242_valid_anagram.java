import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {
		//NOTE: could use one single array for better performance
		// Algo:  
		//    check Length
		//    counter: int[26]
		//    for every c in s: increase counter
		//    for every c in t: decrease counter
		//    assert for every value in counter, value == 0
		
		HashMap<Character, Integer> c1 = new HashMap<>();
		HashMap<Character, Integer> c2 = new HashMap<>();
		for (int i =0 ; i < s.length(); ++i){
			char c = s.charAt(i);
			c1.put(c, c1.getOrDefault(c, 0) + 1);
		}

		for (int i =0 ; i < t.length(); ++i){
			char c = t.charAt(i);
			c2.put(c, c2.getOrDefault(c, 0) + 1);
		}

		return c1.equals(c2);
    } 
}
