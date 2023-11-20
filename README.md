# DBT DuckDB Array and Variables

## Requirement

- duckdb
- sqltools on VSCode

## Profile

Use the following profile to use duckdb on the same folder.

```yml
default:
  outputs:
    dev:
      type: duckdb
  target: dev
```

## Running This DBT Project

Prepare Seeds:
`make generate-seeds`

Then running the following commands:

- dbt seed
- dbt run

It will output a file called `dev.duckdb` in your project workspace`

## Resources:

- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
