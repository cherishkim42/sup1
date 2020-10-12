//"Check Permutation": Given two strings, write a method to decide if one is a permutation of the
// other.

import java.util.HashMap;
import java.util.Map;

public class ProblemTwo {

  public static Map<Character, Integer> makeHistogram(String inputString) {
    char[] inputToArray = inputString.toCharArray();
    Map<Character, Integer> inputDictionary = new HashMap<>();
    for (int i=0; i<inputToArray.length; i++) {
      if (inputDictionary.containsKey(inputToArray[i])) {
        int currentValue = inputDictionary.get(inputToArray[i]);
        currentValue ++;
        inputDictionary.put((inputToArray[i]), currentValue);
      } else {
        inputDictionary.put((inputToArray[i]), 1);
      }
    }
    return inputDictionary;
  }

  public static Boolean isPermutation(String inputStringOne, String inputStringTwo) {
//    char[] inputOneArray = inputStringOne.toCharArray();
//    char[] inputTwoArray = inputStringTwo.toCharArray();

//    if (inputOneArray.length != inputTwoArray.length) {
//      return false;
//    }
    if (inputStringOne.length() != inputStringTwo.length()) {
      return false;
    }

//    Instantiate two dictionary histograms
    Map<Character, Integer> inputOneDictionary = makeHistogram(inputStringOne);
    Map<Character, Integer> inputTwoDictionary = makeHistogram(inputStringTwo);

//    for (int i=0; i<inputOneArray.length; i++) {
//      if (inputOneDictionary.containsKey(inputOneArray[i])) {
//        int currentValue = inputOneDictionary.get(inputOneArray[i]);
//        currentValue ++;
//        inputOneDictionary.put((inputOneArray[i]), currentValue);
//      } else {
//        inputOneDictionary.put((inputOneArray[i]), 1);
//      }
//    }
//
//    for (int i=0; i<inputTwoArray.length; i++) {
//      if (inputTwoDictionary.containsKey(inputTwoArray[i])) {
//        int currentValue = inputTwoDictionary.get(inputTwoArray[i]);
//        currentValue ++;
//        inputTwoDictionary.put((inputTwoArray[i]), currentValue);
//      } else {
//        inputTwoDictionary.put((inputTwoArray[i]), 1);
//      }
//    }

//    car,                    cat
//    {c: 1, a: 1, r: 1}      {c: 1, a: 1, t: 1}
    for (char character : inputOneDictionary.keySet()) {
      if (!inputOneDictionary.get(character).equals(inputTwoDictionary.get(character))) {
        return false;
      }
    } return true;
////    1: car, 2: arc
////    c       a
//    for (char character: inputStringOneToCharArray) {
//        for (char otherCharacter: inputStringTwoToCharArray) {
//          if (character != otherCharacter) {
//            return false;
//          }
//        }
//    } return true;
  }

  public static void main(String[] args) {
    Boolean soutStatement = isPermutation("hello", "olleh");
    Boolean soutStatement2 = isPermutation("cat", "car");
    System.out.println("hello and olleh " + soutStatement);
    System.out.println("cat and car " + soutStatement2);
    //So, the helper function works.
//    Map<Character, Integer> testHelper = makeHistogram("Sally");
//    System.out.println(testHelper);
  }
}

//pseudocode hooray
//Input params: two strings.

//If the length of the two IS the same:
//    Instantiate a dictionary histogram for inputStringOne
//    Instantiate a dictionary histogram for inputStringTwo
//    For each letter in inputStringOne:
//        If it's in the histogram for inputStringOne;

//Else (i.e. if the length of the two IS NOT the same), return false (make this the default return)