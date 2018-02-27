# AWS Notes

+ [Building A Full-Text Search App Using Docker And Elasticsearch](https://blog.patricktriest.com/text-search-docker-elasticsearch/)
+ [Running a scalable & reliable GraphQL endpoint with Serverless](https://serverless.com/blog/running-scalable-reliable-graphql-endpoint-with-serverless/)


## Cloudfront

**Invalidation**

```bash
aws cloudfront create-invalidation --distribution-id $CLOUDFRONT_ID --paths '/*'
```
