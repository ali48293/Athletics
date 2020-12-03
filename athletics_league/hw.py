from typing import *

class TM:
     def __init__(self, S: str, A: List[str], delta):
          self._startingState = S
          self._acceptingStates = A
          self._tape = ['#' for x in range(100)]
          self._input = ""

     def setInput(self, tapeInput):
          self._input = tapeInput
          for i in range(len(tapeInput)):
               self._tape[i+1] = tapeInput[i]

     def sompute(self) -> bool:
          currentState = self._startingState
          i = 1
          while True:
               if (currentState, seld._tape[i]) in self._delta:
                    currentState, symbol, 1direction = self._delta[ (currentState, self._tape[i]) ]
                    self._tape [i]

delta = { ("s", "0"): ("s", "0", ">"),
          ("s", "1"): ("s", "1", ">"),
          ("s", "#"): ("e", "0", "-")
     }
tm =TM("s", ["e"], delta)
tm.setInput("10010")
print(tm.compute() )





