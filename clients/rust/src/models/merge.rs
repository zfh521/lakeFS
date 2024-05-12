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

#[derive(Clone, Default, Debug, PartialEq, Serialize, Deserialize)]
pub struct Merge {
    #[serde(rename = "message", skip_serializing_if = "Option::is_none")]
    pub message: Option<String>,
    #[serde(rename = "metadata", skip_serializing_if = "Option::is_none")]
    pub metadata: Option<std::collections::HashMap<String, String>>,
    /// In case of a merge conflict, this option will force the merge process to automatically favor changes from the dest branch ('dest-wins') or from the source branch('source-wins'). In case no selection is made, the merge process will fail in case of a conflict
    #[serde(rename = "strategy", skip_serializing_if = "Option::is_none")]
    pub strategy: Option<String>,
    #[serde(rename = "force", skip_serializing_if = "Option::is_none")]
    pub force: Option<bool>,
}

impl Merge {
    pub fn new() -> Merge {
        Merge {
            message: None,
            metadata: None,
            strategy: None,
            force: None,
        }
    }
}
