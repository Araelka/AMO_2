pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                // Клонирование репозитория
                git 'https://github.com/Araelka/AMO_2.git'
            }
        }
        stage('Check Workspace') {
            steps {
                // Вывод списка файлов в рабочей директории Jenkins
                bat 'dir'
                // Или на Unix-подобных системах
                // sh 'ls'
            }
        }
    }
}