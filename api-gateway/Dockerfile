FROM eclipse-temurin:17-jdk-alpine
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN apk add --no-cache maven && \
    mvn clean package -DskipTests && \
    apk del maven && \
    rm -rf /root/.m2
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "target/api-gateway-1.0.0.jar"]