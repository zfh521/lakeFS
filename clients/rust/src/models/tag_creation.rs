/*
 * lakeFS API
 *
 * lakeFS HTTP API
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: services@treeverse.io
 * Generated by: https://openapi-generator.tech
 */

use crate::models;

/// TagCreation : Make tag ID point at this REF.
#[derive(Clone, Default, Debug, PartialEq, Serialize, Deserialize)]
pub struct TagCreation {
    /// ID of tag to create
    #[serde(rename = "id")]
    pub id: String,
    /// the commit to tag
    #[serde(rename = "ref")]
    pub r#ref: String,
    #[serde(rename = "force", skip_serializing_if = "Option::is_none")]
    pub force: Option<bool>,
}

impl TagCreation {
    /// Make tag ID point at this REF.
    pub fn new(id: String, r#ref: String) -> TagCreation {
        TagCreation {
            id,
            r#ref,
            force: None,
        }
    }
}
