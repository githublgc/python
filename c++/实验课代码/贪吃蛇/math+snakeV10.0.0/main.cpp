#include <QApplication>
#include "mainform.h"
#include "loginform.h"
#include "widget.h"
#include    "snake.h"
int main(int argc,char** argv)
{
    QApplication app(argc,argv);

    MainForm *main = new MainForm();
    main->setWindowTitle("选择游戏");//设置窗体标题

    MainForm login1;

    Snake *snake=new Snake();//这里成功实现了贪吃蛇，但是注意只有填完对应登录信息和关掉math，点snake按键后才能开始使用。
    {snake->show();}

     MainForm login2;//这里成功实现了计算器的使用，但是注意只有填完对应登录信息和点math按键后才能开始使用。
     Widget *widget= new Widget();

    {widget->show();}

    LoginForm login;
    if (login.exec() == QDialog::Accepted)//调用login.exec()，阻塞主控制流，直到完成返回，继续执行主控制流
    {
       main->show();
       return app.exec();
    }
    else return 0;

    LoginForm hint;//实现弹窗，1.需要在主函数加声明。







    /*MainForm login;
    if (login.exec() == QDialog::Accepted)//调用login.exec()，阻塞主控制流，直到完成返回，继续执行主控制流
    {
       main->show();
       return app.exec();
    }
    else return 0;*/
}
