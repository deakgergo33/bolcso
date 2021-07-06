package com.project.bolcso;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@EnableScheduling
@SpringBootApplication
public class BolcsoApplication {

	public static void main(String[] args) {
		SpringApplication.run(BolcsoApplication.class, args);
	}

}
