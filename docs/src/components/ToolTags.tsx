import { motion } from "framer-motion";
import React from "react";
import tools from "../constants/toolsData";
import { Badge } from "./ui/badge";

const ToolTags: React.FC = () => {
	const toolName = document.location.pathname.split('/').pop()?.replace('.mdx', '');
	const tool = tools.find(
		(t) => t.name.toLowerCase() === toolName?.toLowerCase()
	);

	if (!tool) {
		return null;
	}

	return (
		<div className="flex flex-wrap gap-2 mb-4">
			{tool.tags.map((tag) => (
				<motion.div
					key={tag}
					whileHover={{ scale: 1.05 }}
					whileTap={{ scale: 0.95 }}
					className="cursor-pointer"
				>
					<Badge
						variant="outline"
						className="bg-white text-gray-800 border-gray-300 hover:bg-gradient-to-r from-purple-500 to-indigo-500 hover:text-white shadow-lg transition duration-200 ease-in-out transform"
					>
						{tag}
					</Badge>
				</motion.div>
			))}
		</div>
	);
};

export default ToolTags;
