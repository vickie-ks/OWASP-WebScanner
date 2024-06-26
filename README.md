# OWASP-WebScanner

Welcome to the OWASP-WebScanner project! This cutting-edge AI-driven tool is designed to enhance the security of web applications by meticulously scanning for the top 10 OWASP security risks. Utilizing advanced machine learning algorithms, OWASP-WebScanner efficiently identifies vulnerabilities, providing detailed reports to safeguard your digital assets.

## Key Features

- **AI-Driven Analysis:** Leverages machine learning to pinpoint and categorize security vulnerabilities with high precision.
- **Comprehensive Scanning:** Targets the latest OWASP Top 10 security risks to ensure your web application remains secure against emerging threats.
- **Detailed Reporting:** Offers in-depth vulnerability reports that help developers understand and mitigate identified issues promptly.

### Targeted OWASP Top 10 Client-Side Security Risks

Here are the specific client-side security risks that OWASP-WebScanner focuses on:

| OWASP Client-Side Security Risks              | Definition                                                                                                                                                                                                                 |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Broken Client-side Access Control                    | A website allows users to delete posts via a JavaScript function deletePost(postId). An attacker can invoke this function directly from their browser console without proper checks, deleting posts they shouldn't access. |
| DOM-based XSS                                        | A webpage uses JavaScript to display user input from URL parameters directly into the DOM without sanitization, enabling an attacker to craft a URL that injects and executes a malicious script.                          |
| Sensitive Data Leakage                               | A website's JavaScript code contains API keys or user session tokens that can be easily accessed by viewing the source code.                                                                                               |
| Vulnerable and Outdated Components                   | A website using an outdated jQuery library that contains known vulnerabilities, allowing XSS or other attacks.                                                                                                             |
| Lack of Third-party Origin Control                   | A webpage allows content to be loaded from any third-party URL without a Content Security Policy (CSP), potentially leading to malicious content being loaded.                                                             |
| JavaScript Drift                                     | A website's JavaScript functionality changes after dynamically loading new scripts, but the changes introduce security flaws because they were not reviewed as thoroughly as the original script.                          |
| Sensitive Data Stored Client-Side                    | A web application stores encrypted user credentials in localStorage, but an XSS vulnerability allows an attacker to access and decrypt this information.                                                                   |
| Client-side Security Logging and Monitoring Failures | A web application does not log failed login attempts or script errors on the client side, missing out on indications of attack attempts or misconfigurations.                                                              |
| Not Using Standard Browser Security Controls         | A site does not set SameSite attributes on cookies, allowing potentially dangerous cross-site request forgery (CSRF) attacks.                                                                                              |
| Including Proprietary Information on the Client-Side | A financial application performs critical calculations and decision-making processes in JavaScript, exposed to any user who inspects the web page's source.                                                                |

For more details about these client-side security risks, [click here](https://owasp.org/www-project-top-10-client-side-security-risks/).
