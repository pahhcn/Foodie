package com;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;
import org.springframework.context.event.EventListener;
import org.springframework.core.env.Environment;

@SpringBootApplication
@MapperScan(basePackages = {"com.dao"})
public class SpringbootSchemaApplication extends SpringBootServletInitializer{

	private final Environment environment;

	public SpringbootSchemaApplication(Environment environment) {
		this.environment = environment;
	}

	public static void main(String[] args) {
		SpringApplication.run(SpringbootSchemaApplication.class, args);
	}
	
	@Override
    protected SpringApplicationBuilder configure(SpringApplicationBuilder applicationBuilder) {
        return applicationBuilder.sources(SpringbootSchemaApplication.class);
    }

	@EventListener(ApplicationReadyEvent.class)
	public void printAccessUrls() {
		String port = environment.getProperty("server.port", "8080");
		String contextPath = environment.getProperty("server.servlet.context-path", "");
		String baseUrl = "http://localhost:" + port + contextPath;
		
		System.out.println("\n========================================");
		System.out.println("应用启动成功！");
		System.out.println("========================================");
		System.out.println("前台地址: " + baseUrl + "/front/index.html");
		System.out.println("后台地址: " + baseUrl + "/admin/dist/index.html");
		System.out.println("========================================");
		System.out.println("管理员账号: abo");
		System.out.println("管理员密码: abo");
		System.out.println("========================================\n");
	}
}
