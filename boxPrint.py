import traceback
def boxPrint(symbol, width, height):
   # if len(symbol) != 1:
   #     raise Exception('Only one character for symbols.')
    assert len(symbol) == 1, 'Symbol is not one character long.'
   # if(width < 2) or (height < 2):
   #     raise Exception('Width or height is less than two.')
    assert (width >= 2), 'Width is less than two.'
    assert (height >= 2), 'Height is less than two.'
    print(symbol * width)

    for i in range(height - 2):
        print(symbol+ (' ' * (width - 2)) + symbol)
    print(symbol * width)

boxPrint('*', 2, 2)
