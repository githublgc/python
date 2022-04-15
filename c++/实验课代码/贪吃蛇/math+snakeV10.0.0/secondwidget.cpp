#include "secondwidget.h"
#include "ui_secondwidget.h"

secondwidget::secondwidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::secondwidget)
{
    ui->setupUi(this);
}

secondwidget::~secondwidget()
{
    delete ui;
}
