//"Is Unique": Implement an algorithm to determine if a string has all unique characters.
// What if you cannot use additional data structures?
import java.util.HashSet;

public class ProblemOne {

  //  version without additional data structures, O(n^2) runtime
  public static Boolean hasDuplicate(String inputString) {
    for (int i=0; i<inputString.length(); i++) { //O(n)
      for (int j=i+1; j<inputString.length(); j++) { //O(n)
        char resultI = inputString.charAt(i); //O(1)
        char resultJ = inputString.charAt(j); //O(1)
        if (resultI == resultJ) {
          return true;
        }
      }
    } return false;
  }

  //  version with additional data structure (hashmap implemented w/ hashset)
//  optimizes runtime -- O(n) because sets have constant lookup
  public static Boolean hasDuplicateHash(String inputString) {
    HashSet<Character> hashsetifiedInput = new HashSet<>();
    for (int i=0; i<inputString.length(); i++) {
      char resultI = inputString.charAt(i);
      if (hashsetifiedInput.contains(resultI)) {
        return true;
      } else {
        hashsetifiedInput.add(resultI);
      }
    } return false;
  }

  public static void main(String[] args) {
    Boolean returnMe = hasDuplicateHash("heckle");
    System.out.println(returnMe);
  }
};

//Set a variable equal to the letter at the first index of the input string
//Iterate through the input string
//For each letter in the input string after the first unit
//  if the letter matches the value of the variable, return false.
//   in any case, switch
//If you make it to the end without that ever happening, return true.

//for i in input_array:
//    for j in input_array:
//        if input_array[i] == input_array[j]:
//            return True
//        j++;
//      i++;

//abcb
//i=0
//j=i+1