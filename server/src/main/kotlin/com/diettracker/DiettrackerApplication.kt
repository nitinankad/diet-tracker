package com.diettracker

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class DiettrackerApplication

fun main(args: Array<String>) {
	runApplication<DiettrackerApplication>(*args)
}
