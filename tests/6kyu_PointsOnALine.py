# (x2−x1)(y3−y1)=(x3−x1)(y2−y1)



def on_line(points):
    if len(points) <=2:
        return True
    else:
        start_point = 0
        end_point = 3
        while end_point <= len(points):
            wp = points[start_point:end_point] # vector product method
            vector_product_1 = (wp[1][0] - wp[0][0]) * (wp[2][1] - wp[0][1])
            vector_product_2 = (wp[2][0] - wp[0][0]) * (wp[1][1] - wp[0][1])
            if vector_product_1 == vector_product_2:
                start_point += 1
                end_point += 1
            else:
                return False
        return True




print(on_line(((5,10), (6,12), (7,14), (10,20), (23,46), (17,34))))
print(on_line(((5,10), (6,12), (7,14), (10,20), (23,46), (17,35))))
