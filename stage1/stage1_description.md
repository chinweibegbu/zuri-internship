# Stage 1

## Task Details

### Overview
Create and host an endpoint using any programming language of your choice. The endpoint should take two GET parameters and return specific information in JSON format. 

### Language Options
* Python
* Golang
* NodeJS
* PHP

### Information Required 
1. Slack name
2. Current day of the week
3. Current UTC time (with validation of +/-2)
4. Track
5. GitHub URL of the file being run
6. The GitHub URL of the full source code

### JSON
```
{
    "slack_name": "example_name",
    "current_day": "Monday",
    "utc_time": "2023-08-21T15:04:05Z",
    "track": "Frontend",
    "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
    "github_repo_url": "https://github.com/username/repo",
    "status_code": "200"
}
```

## Acceptance Criteria
1. **Endpoint Creation**: Provide a publicly accessible endpoint.
2. **GET Parameters**: The endpoint should accept two GET parameters: slack_name and track. E.g., http://example.com/api?slack_name=example_name&track=frontend.
3. **JSON Components**
   * **Slack Name**: The response should include the slack_name passed as a GET parameter.
   * **Current Day of the Week**: Display the current day of the week in full (e.g., Monday, Tuesday, etc.).
   * **Current UTC Time**: Return the current UTC time, accurate within a +/-2 minutes window.
   * **Track**: The response should display the track of the person, which can be "frontend", "backend", "fullstack", etc. This will be based on the track GET parameter passed to the endpoint.
   * **GitHub File URL**: Include a direct link to the specific file in the GitHub repository that's being executed.
   * **GitHub Repo URL**: Include a link to the main page of the GitHub repository containing the project's entire source code.
   * **Status Code**: Return 200 as a String 
4. **JSON Format**: The endpoint's response should adhere to the specified JSON format.

## Testing
Before submission:
- [ ] Ensure the endpoint is accessible
- [ ] Check the returned JSON against the defined format
- [ ] Validate the correctness of each data point in the JSON response
