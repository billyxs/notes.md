# AWS Notes

- [Building A Full-Text Search App Using Docker And Elasticsearch](https://blog.patricktriest.com/text-search-docker-elasticsearch/)
- [Running a scalable & reliable GraphQL endpoint with Serverless](https://serverless.com/blog/running-scalable-reliable-graphql-endpoint-with-serverless/)
- [Z-Order Indexing for Multifaceted DynamoDB Queries: Part 1](https://aws.amazon.com/blogs/database/z-order-indexing-for-multifaceted-queries-in-amazon-dynamodb-part-1/)

## Monitoring

- [Client side monitoring - open source](https://desole.io/)

## Cloudfront

**Invalidation**

```bash
aws cloudfront create-invalidation --distribution-id $CLOUDFRONT_ID --paths '/*'
```
