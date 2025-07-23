//Interger.h
#ifndef INTEGER_H
#define INTEGER_H

class integer {
public:
    integer(const int& the_int);
    int get_int() const;
    integer operator+(const integer& other_integer) const;
private:
    int _the_int;
};

#endif // INTEGER_H