pipeline {
    agent any
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/Araelka/AMO_2.git'
            }
        }
        
        // stage('Install dependencies') {
        //     steps {
        //         sh 'pip install -r requirements.txt'
        //     }
        // }
        // stage('Сбор данных') {
        //     steps {
        //         script {
        //             // Выполняем Python скрипт для загрузки данных
        //             bat 'python load_data.py'
        //         }
        //     }
        // }
        // stage('Подготовка данных') {
        //     steps {
        //         script {
        //             // Выполняем Python скрипт для подготовки данных
        //             bat 'python prepare_data.py'
        //         }
        //     }
        // }
        // stage('Обучение модели') {
        //     steps {
        //         script {
        //             // Выполняем Python скрипт для обучения модели
        //             bat 'python train_model.py'
        //         }
        //     }
        // }
        // stage('Анализ модели') {
        //     steps {
        //         script {
        //             // Выполняем Python скрипт для анализа модели
        //             bat 'python evaluate_model.py'
        //         }
        //     }
        // }
    }
}