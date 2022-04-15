#include "widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
{
    layout1=new QHBoxLayout;
    layout2=new QHBoxLayout;

    layout4=new QGridLayout(this);

    btn1=new QPushButton;
    edit1=new QLineEdit;
    edit2=new QLineEdit;
    edit3=new QLineEdit;
     label1=new QLabel;


 layout4->addWidget(btn1,0,0);
 layout4->addWidget(edit1,0,1);
 layout4->addWidget(edit2,0,2);
 layout4->addWidget(edit3,0,3);

  layout4->addWidget(label1,1,2);
   btn1->setText("计算");

connect(btn1,SIGNAL(clicked()),this,SLOT(on_clicked()));
}

Widget::~Widget()
{

}
void Widget::on_clicked()
{
       int a = edit1->text().toInt();//第一个空输入
        int b = edit3->text().toInt();//后一个操作数在第三个上面的输入
        if (edit2->text() == "+")//通过分析第二个空输入的字符来判断进行什么功能
            label1->setText(QString::number(a + b));
        if (edit2->text() == "-")
            label1->setText(QString::number(a - b));
        if (edit2->text() == "*")
            label1->setText(QString::number(a * b));
        if (edit2->text() == "/")
        {
            if (b != 0)
                label1->setText(QString::number(a / b));
        }
        if (edit2->text() == "%")//     增加新功能
        {
            if (b != 0)
                label1->setText(QString::number(a % b));
        }
}
