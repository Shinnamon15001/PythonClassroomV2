class Calculate_area:
    def retangle_area(self, w, h):
        return w * h
    
    @classmethod
    def triangle_area(cls, b, h):
        return 0.5 * b * h
    
    @staticmethod
    def circle_area(r):
        return 3.14 * r * r 
    
cal = Calculate_area()
cal_rec = cal.retangle_area(4, 5)
cal_tri = cal.triangle_area(4, 5)
cal_cir = cal.circle_area(5)

# print("Rectangle Area = ", cal_rec)
# print("Triangle Area = ", cal_tri)
# print("Circle Area = ", cal_cir)

print("Test Retangle Area", Calculate_area.retangle_area(4, 5))
print("Test Triangle Area", Calculate_area.triangle_area(4, 5))
print("Test Circle Area", Calculate_area.circle_area(5))